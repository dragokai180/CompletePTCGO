from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d0d26742-1b44-5f0e-93b7-846c0e4a789c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name',
    display_name='Whiscash',
    searchable_by=['Whiscash', 'Stage 1', 'Whiscash'],
    subtypes=['Stage 1'],
    collector_number=109,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name',
    family_id=339,
    abilities=[
        Attack(
            title='Raging and Rocking',
            game_text="For each Fighting Energy attached to this Pokémon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Land Crush',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
