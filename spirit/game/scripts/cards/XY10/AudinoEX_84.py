from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='407b225d-4a96-5f64-bb4b-a02336dc918c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AudinoEX.Name',
    display_name='Audino-EX',
    searchable_by=['Audino-EX', 'Basic', 'EX', 'AudinoEX'],
    subtypes=['Basic', 'EX'],
    collector_number=84,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=531,
    abilities=[
        Attack(
            title='Drain Slap',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Do the Wave',
            game_text='This attack does 10 more damage for each of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
