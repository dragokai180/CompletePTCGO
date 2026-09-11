from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3ff6d4c-779c-5706-9662-ba1a8cf9ffa0',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name',
    display_name='Stonjourner',
    searchable_by=['Stonjourner', 'Basic', 'Stonjourner'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=874,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Mega Kick',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
