from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94c3ef74-249a-57f0-87a5-b582c5704054',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name',
    display_name='Fearow',
    searchable_by=['Fearow', 'Stage 1', 'Fearow'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    family_id=21,
    abilities=[
        Attack(
            title='Beak Catch',
            game_text='Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
