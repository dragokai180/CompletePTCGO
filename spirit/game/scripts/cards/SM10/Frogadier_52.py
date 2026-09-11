from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24dc1611-8aca-5c33-a2fc-9334540f46e3',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    display_name='Frogadier',
    searchable_by=['Frogadier', 'Stage 1', 'Frogadier'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    family_id=656,
    abilities=[
        Attack(
            title='Afterimage Strike',
            game_text="If any damage is done to this Pokémon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
