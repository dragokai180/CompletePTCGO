from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='25435822-4b51-5a8e-a431-fad35991f19a',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name',
    display_name='Registeel',
    searchable_by=['Registeel', 'Basic', 'Registeel'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Silver Fist',
            game_text="If your opponent's Active Pokémon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
