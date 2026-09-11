from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d312879-9971-50ad-843e-fc048418c8fe',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name',
    display_name='Corsola',
    searchable_by=['Corsola', 'Basic', 'Corsola'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=222,
    abilities=[
        Attack(
            title='Recover',
            game_text='Discard a Water Energy attached to Corsola and remove all damage counters from Corsola.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hyper Cannon',
            game_text='Flip 2 coins. If both of them are heads, this attack does 20 damage plus 50 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
