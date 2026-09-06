from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_fighting_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIGHTING.value)


async def aura_jab(ctx):
    """130. Attach up to 3 Basic Fighting Energy cards from your discard pile
    to your Benched Pokémon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    energies = [c for c in ctx.discard_pile() if _is_basic_fighting_energy(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 3, minimum=0,
        prompt="Choose up to 3 Basic Fighting Energy cards to attach to your Benched Pokémon",
    )
    if picks:
        await distribute_energy(ctx, picks, bench)

card = PokemonCardDef(
    guid="afe4a58d-5b31-5ee7-87ff-adabd8950d01",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLucarioex.Name",
    display_name="Mega Lucario ex",
    searchable_by=["Mega Lucario ex","SV_Mega","ex","Stage 1","MegaLucarioex"],
    subtypes=["SV_Mega","ex","Stage 1"],
    collector_number=77,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Aura Jab",
            game_text="Attach up to 3 Basic Fighting Energy cards from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=aura_jab,
        ),
        Attack(
            title="Mega Brave",
            game_text="During your next turn, this Pokémon can't use Mega Brave.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=270,
            locks_next_turn=True,
        ),
    ],
)
