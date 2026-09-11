from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f473f10-81fe-534b-9b28-fc305e7a8651',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GumshoosGX.Name',
    display_name='Gumshoos-GX',
    searchable_by=['Gumshoos-GX', 'Stage 1', 'GX', 'GumshoosGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=110,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name',
    family_id=734,
    abilities=[
        Ability(
            title='Search the Premises',
            game_text='Once during your turn (before your attack), you may have your opponent reveal their hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title='Gumshoe Chance-GX',
            game_text="This attack does 50 damage times the amount of Energy attached to your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
