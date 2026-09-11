from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77b5d91a-ea5f-5357-8c77-fb39f379aa69',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name',
    display_name='Mightyena',
    searchable_by=['Mightyena', 'Stage 1', 'Mightyena'],
    subtypes=['Stage 1'],
    collector_number=87,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name',
    family_id=261,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title='Dark Fang',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
