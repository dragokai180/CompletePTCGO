from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c2fdd98-9ac4-5c64-a516-715bf4bbacda',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name',
    display_name='Huntail',
    searchable_by=['Huntail', 'Stage 1', 'Huntail'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name',
    family_id=366,
    abilities=[
        Attack(
            title='Big Bite',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dangerous Bite',
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
