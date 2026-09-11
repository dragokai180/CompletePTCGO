from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f77be2dd-6f59-52ef-b41d-863a8f84ebf7',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name',
    display_name='Venusaur',
    searchable_by=['Venusaur', 'Stage 2', 'Venusaur'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name',
    family_id=1,
    abilities=[
        Ability(
            title='Jungle Totem',
            game_text="Each basic Grass Energy attached to your Pokémon provides GrassGrass Energy. You can't apply more than 1 Jungle Totem Ability at a time.",
            passive=standard_passive("Each basic Grass Energy attached to your Pokémon provides GrassGrass Energy. You can't apply more than 1 Jungle Totem Ability at a time."),
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
