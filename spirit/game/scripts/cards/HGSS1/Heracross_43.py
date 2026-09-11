from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0fb09ee-f05a-5780-9916-d24f632d1235',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name',
    display_name='Heracross',
    searchable_by=['Heracross', 'Basic', 'Heracross'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title='Green Draw',
            game_text='Draw a card for each of your Grass Pokémon in play.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double Headbutt',
            game_text='Flip 2 coins. This attack does 30 damage plus 20 more damage for each heads.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
