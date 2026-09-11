from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='358e25b7-fe8c-5daf-b70e-9f5b65369acf',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name',
    display_name='Volcarona',
    searchable_by=['Volcarona', 'Stage 1', 'Volcarona'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    family_id=636,
    abilities=[
        Ability(
            title='Heat Cyclone',
            game_text='Once during your turn (before your attack), you may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
