from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.bw10 import CursedGlarePassive, blizzard
from spirit.game.card_effects.pokemon import is_pokemon_vmax
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="1459a43f-6a80-5644-bc1e-545330ea097c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus","Basic","Landorus"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Abundant Harvest",
            game_text="Attach a basic Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Gaia Hammer",
            game_text="Does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=blizzard,
        ),
    ],
)
