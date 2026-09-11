from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21daeca1-d526-59f7-b896-8a77e92444b0',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name',
    display_name='Empoleon',
    searchable_by=['Empoleon', 'Stage 2', 'Empoleon'],
    subtypes=['Stage 2'],
    collector_number=56,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name',
    family_id=393,
    abilities=[
        Attack(
            title='Recall',
            game_text="Choose an attack from 1 of this Pokémon's previous Evolutions and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aquafall',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
