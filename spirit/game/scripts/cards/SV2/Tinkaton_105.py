from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c52bdf00-812f-5820-b122-a121b5a41e90',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name',
    display_name='Tinkaton',
    searchable_by=['Tinkaton', 'Stage 2', 'Tinkaton'],
    subtypes=['Stage 2'],
    collector_number=105,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    family_id=957,
    abilities=[
        Ability(
            title='Gather Materials',
            game_text='You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Special Hammer',
            game_text='If this Pokémon has any Special Energy attached, this attack does 90 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
