from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b426e269-305a-5ce2-a51e-3f01d56b2bdd',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AegislashEX.Name',
    display_name='Aegislash-EX',
    searchable_by=['Aegislash-EX', 'Basic', 'EX', 'AegislashEX'],
    subtypes=['Basic', 'EX'],
    collector_number=65,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=681,
    abilities=[
        Ability(
            title='Mighty Shield',
            game_text="Prevent all damage done to this Pokémon by attacks from each of your opponent's Pokémon that has any Special Energy attached to it.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from each of your opponent's Pokémon that has any Special Energy attached to it."),
        ),
        Attack(
            title='Slash Blast',
            game_text='This attack does 20 more damage for each Metal Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
