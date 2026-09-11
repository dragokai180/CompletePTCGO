from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f1f1f1a-37d8-5c53-bfb4-076d7a321919',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name',
    display_name='Cyclizar ex',
    searchable_by=['Cyclizar ex', 'Basic', 'ex', 'Cyclizarex'],
    subtypes=['Basic', 'ex'],
    collector_number=18,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title='Power Run',
            game_text='Search your deck for a Basic Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Full Throttle',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
