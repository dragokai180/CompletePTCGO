from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b3666e0b-18e0-54db-bd64-00de3d6b2b25',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotex.Name',
    display_name='Pidgeot ex',
    searchable_by=['Pidgeot ex', 'Stage 2', 'ex', 'Pidgeotex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=164,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    family_id=16,
    abilities=[
        Ability(
            title='Quick Search',
            game_text="Once during your turn, you may search your deck for a card and put it into your hand. Then, shuffle your deck. You can't use more than 1 Quick Search Ability each turn.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Blustery Wind',
            game_text='You may discard a Stadium in play.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
