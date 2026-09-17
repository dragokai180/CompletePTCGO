from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b01990a-8ca5-5cd6-aed9-57676009b8d2',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name',
    display_name='Revavroom',
    searchable_by=['Revavroom', 'Stage 1', 'Revavroom'],
    subtypes=['Stage 1'],
    collector_number=142,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name',
    family_id=965,
    abilities=[
        Ability(
            title='Rumbling Engine',
            game_text='You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 90 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
