from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8cae49b3-008d-557a-a23f-28662866bc00',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name',
    display_name='Charizard',
    searchable_by=['Charizard', 'Stage 2', 'Charizard'],
    subtypes=['Stage 2'],
    collector_number=158,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=6,
    abilities=[
        Ability(
            title='Roaring Resolve',
            game_text='Once during your turn (before your attack), you may put 2 damage counters on this Pokémon. If you do, search your deck for up to 2 Fire Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Continuous Blaze Ball',
            game_text='Discard all Fire Energy from this Pokémon. This attack does 50 more damage for each card you discarded in this way.',
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
