from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9d27df7-8f09-5ca0-8078-b650eba9e7b3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowscarada.Name',
    display_name='Meowscarada',
    searchable_by=['Meowscarada', 'Stage 2', 'Meowscarada'],
    subtypes=['Stage 2'],
    collector_number=15,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name',
    family_id=906,
    abilities=[
        Attack(
            title='Trick Cape',
            game_text="You may put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Flower Blast',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
