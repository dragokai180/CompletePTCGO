from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.card_effects.trainers import is_basic_energy_card


async def flashing_spear(ctx):
    """You may discard up to 2 Basic Energy from your Benched Pokémon. This
    attack does 90 more damage for each card you discarded in this way."""
    pool = [
        energy
        for pokemon in ctx.my_bench()
        for energy in ctx.attached_energies(pokemon)
        if is_basic_energy_card(energy)
    ]
    discarded = []
    if pool:
        discarded = await ctx.choose_cards(
            pool, min(2, len(pool)), minimum=0,
            prompt="Choose up to 2 Basic Energy to discard from your Benched Pokémon",
        )
        if discarded:
            await ctx.discard_cards(discarded)
    await ctx.deal_damage(60 + 90 * len(discarded))


card = PokemonCardDef(
    guid="2f9e03ca-d726-5ef8-bfc7-a6bb8caf886b",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteonex.Name",
    display_name="Jolteon ex",
    searchable_by=["Jolteon ex","Stage 1","ex","Tera","Jolteonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=30,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Flashing Spear",
            game_text="You may discard up to 2 Basic Energy from your Benched Pokémon. This attack does 90 more damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=flashing_spear,
        ),
        Attack(
            title="Dravite",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            locks_next_turn=True,
        ),
    ],
)
