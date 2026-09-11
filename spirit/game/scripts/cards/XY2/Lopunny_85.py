from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='690c6029-bae0-5aae-8dcd-bb1d586144f3',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name',
    display_name='Lopunny',
    searchable_by=['Lopunny', 'Stage 1', 'Lopunny'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name',
    family_id=427,
    abilities=[
        Ability(
            title='Big Jump',
            game_text='Once during your turn (before your attack), you may return this Pokémon and all cards attached to it to your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sitdown Bounce',
            game_text="Flip a coin. If tails, this Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
