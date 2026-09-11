from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd394b41-b2da-5015-9c55-0598f4c1ac59',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name',
    display_name='Scizor',
    searchable_by=['Scizor', 'Stage 1', 'Scizor'],
    subtypes=['Stage 1'],
    collector_number=141,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    family_id=123,
    abilities=[
        Attack(
            title='Punishing Scissors',
            game_text="This attack does 50 more damage for each of your opponent's Pokémon in play that has an Ability.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Cut',
            cost={PokemonTypes.METAL: 2},
            damage=70,
        ),
    ],
)
