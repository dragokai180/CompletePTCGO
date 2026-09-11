from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0b2a2362-7f62-5344-8df3-21d658cbb505',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name',
    display_name='Magcargo',
    searchable_by=['Magcargo', 'Stage 1', 'Magcargo'],
    subtypes=['Stage 1'],
    collector_number=24,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Ability(
            title='Smooth Over',
            game_text='Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
