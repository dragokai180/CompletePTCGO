from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7db7f59-9421-5b2a-a5ab-7b447333b811',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name',
    display_name='Dodrio',
    searchable_by=['Dodrio', 'Stage 1', 'Dodrio'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    family_id=84,
    abilities=[
        Ability(
            title='Zooming Draw',
            game_text='Once during your turn, you may put 1 damage counter on this Pokémon. If you do, draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Ballistic Beak',
            game_text='This attack does 30 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
