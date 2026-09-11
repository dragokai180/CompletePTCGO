from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='30ac4bdd-8d63-5f9b-9ce9-69d818a76a10',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name',
    display_name='Araquanid',
    searchable_by=['Araquanid', 'Stage 1', 'Araquanid'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    family_id=751,
    abilities=[
        Attack(
            title='Bubble Net',
            game_text="Energy can't be attached to the Defending Pokémon from your opponent's hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
