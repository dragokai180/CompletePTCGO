from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc0e4034-e960-5ef7-913c-232050f9c3b0',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name',
    display_name='Ursaring',
    searchable_by=['Ursaring', 'Stage 1', 'Ursaring'],
    subtypes=['Stage 1'],
    collector_number=172,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    family_id=216,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Heavy Hold',
            game_text="The Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
