from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='253993bd-d480-54e0-90c6-d9691570f58a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name',
    display_name='Bouffalant',
    searchable_by=['Bouffalant', 'Basic', 'Bouffalant'],
    subtypes=['Basic'],
    collector_number=174,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=626,
    abilities=[
        Ability(
            title='Bouffer',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Damage Rush',
            game_text='Flip a coin until you get tails. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
