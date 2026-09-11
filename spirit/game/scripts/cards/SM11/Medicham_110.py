from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b98d8774-25a8-5d8e-ba8b-764df056420a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name',
    display_name='Medicham',
    searchable_by=['Medicham', 'Stage 1', 'Medicham'],
    subtypes=['Stage 1'],
    collector_number=110,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    family_id=307,
    abilities=[
        Attack(
            title='Pure Power',
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Master Strike',
            game_text='If this Pokémon has a Karate Belt card attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
