from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_lightning_pokemon(pokemon):
    return PokemonTypes.LIGHTNING.value in (
        pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    )


async def overvolt_discharge(ctx):
    """Attach up to 3 Basic Energy from discard to Lightning Pokémon, then
    this Pokémon is Knocked Out."""
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    lightning = [p for p in ctx.my_pokemon_in_play() if _is_lightning_pokemon(p)]
    if energies and lightning:
        picks = await ctx.choose_cards(
            energies, min(3, len(energies)), minimum=0,
            prompt="Choose up to 3 Basic Energy cards to attach.",
        )
        if picks:
            await distribute_energy(ctx, picks, lightning)
    await ctx.knock_out(ctx.source)


card = PokemonCardDef(
    guid="384dcac4-731a-569a-ba26-0d75f8846623",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton","Stage 1","Magneton"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    family_id=81,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    abilities=[
        Ability(
            title="Overvolt Discharge",
            game_text="Once during your turn, you may attach up to 3 Basic Energy cards from your discard pile to your Lightning Pokémon in any way you like. If you use this Ability, this Pokémon is Knocked Out.",
            activation=Activations.ONCE_PER_TURN,
            effect=overvolt_discharge,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
