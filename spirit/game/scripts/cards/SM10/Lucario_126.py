from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1f361240-5eec-52ae-8aa7-dcb7be37d9f4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name',
    display_name='Lucario',
    searchable_by=['Lucario', 'Stage 1', 'Lucario'],
    subtypes=['Stage 1'],
    collector_number=126,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=447,
    abilities=[
        Attack(
            title='Low Sweep',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Rush Up',
            game_text='If you attached a Pokémon Tool card from your hand to this Pokémon during this turn, this attack does 70 more damage.',
            cost={PokemonTypes.METAL: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
