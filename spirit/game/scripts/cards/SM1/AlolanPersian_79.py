from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='730d76e3-01e2-52f2-bfaf-5d171f8094cd',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanPersian.Name',
    display_name='Alolan Persian',
    searchable_by=['Alolan Persian', 'Stage 1', 'AlolanPersian'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    family_id=52,
    abilities=[
        Attack(
            title='Taunt',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Claw Rend',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
