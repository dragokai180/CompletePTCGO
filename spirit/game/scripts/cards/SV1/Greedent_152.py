from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='755cd263-7c23-5df5-bad9-7a32ef96ba1c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name',
    display_name='Greedent',
    searchable_by=['Greedent', 'Stage 1', 'Greedent'],
    subtypes=['Stage 1'],
    collector_number=152,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name',
    family_id=819,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Enhanced Fang',
            game_text='If this Pokémon has a Pokémon Tool attached, this attack does 80 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
