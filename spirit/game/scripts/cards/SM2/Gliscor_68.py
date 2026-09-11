from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1eab73c3-6b4a-51c0-a720-c2673b9200b3',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name',
    display_name='Gliscor',
    searchable_by=['Gliscor', 'Stage 1', 'Gliscor'],
    subtypes=['Stage 1'],
    collector_number=68,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    family_id=207,
    abilities=[
        Attack(
            title='Finishing Stinger',
            game_text="If your opponent's Active Pokémon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Guillotine',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
