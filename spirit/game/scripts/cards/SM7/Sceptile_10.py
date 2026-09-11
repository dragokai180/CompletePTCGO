from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c60aff5-aa98-57d8-bdfd-b5cf4d8330e1',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name',
    display_name='Sceptile',
    searchable_by=['Sceptile', 'Stage 2', 'Sceptile'],
    subtypes=['Stage 2'],
    collector_number=10,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    family_id=252,
    abilities=[
        Ability(
            title='Power of Nature',
            game_text="Prevent all damage done to your Pokémon that have any Grass Energy attached to them by attacks from your opponent's Ultra Beasts.",
            passive=standard_passive("Prevent all damage done to your Pokémon that have any Grass Energy attached to them by attacks from your opponent's Ultra Beasts."),
        ),
        Attack(
            title='Powerful Storm',
            game_text='This attack does 20 damage times the amount of Energy attached to all of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
