from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ff86edea-6d3c-59e6-9f37-795e495299b1',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name',
    display_name='Incineroar',
    searchable_by=['Incineroar', 'Stage 2', 'Incineroar'],
    subtypes=['Stage 2'],
    collector_number=29,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    family_id=725,
    abilities=[
        Ability(
            title='Strong Cheer',
            game_text="Your Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You can't apply more than 1 Strong Cheer Ability at a time.",
            passive=standard_passive("Your Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You can't apply more than 1 Strong Cheer Ability at a time."),
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
