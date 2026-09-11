from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d436ca01-6786-5374-9273-af463a7b5ddd',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name',
    display_name='Hippowdon',
    searchable_by=['Hippowdon', 'Stage 1', 'Hippowdon'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name',
    family_id=449,
    abilities=[
        Attack(
            title='Resistance Desert',
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pokémon by Pokémon-EX.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
