from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a7715e0-3b88-57d1-922c-286d5a6df451',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name',
    display_name='Electivire',
    searchable_by=['Electivire', 'Stage 1', 'Electivire'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    family_id=125,
    abilities=[
        Attack(
            title='Tag Team Spark',
            game_text='This attack does 20 more damage for each Energy attached to your Magmortar.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Gigavolt',
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
