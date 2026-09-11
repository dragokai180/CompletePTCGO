from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='079af3bf-5083-57e8-b546-f833686f91bf',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name',
    display_name='Zapdos ex',
    searchable_by=['Zapdos ex', 'Basic', 'ex', 'Zapdosex'],
    subtypes=['Basic', 'ex'],
    collector_number=145,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=145,
    abilities=[
        Ability(
            title='Voltaic Float',
            game_text='If this Pokémon has any Lightning Energy attached, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Lightning Energy attached, it has no Retreat Cost.'),
        ),
        Attack(
            title='Multishot Lightning',
            game_text="This attack also does 90 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
