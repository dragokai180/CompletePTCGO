from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.bw10 import DriftingBalloonPassive, derail
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="96898390-5210-5e48-ab25-4d2011c7a8bc",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp","Stage 2","Garchomp"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    abilities=[
        Attack(
            title="Mach Cut",
            game_text="Discard a Special Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=derail,
        ),
        Attack(
            title="Dragonblade",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=mill_attack(2, opponent=False),
        ),
    ],
)
