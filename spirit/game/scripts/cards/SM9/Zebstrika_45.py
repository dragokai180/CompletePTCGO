from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='06756061-e0cd-5f97-86b4-971b0fbdbb68',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name',
    display_name='Zebstrika',
    searchable_by=['Zebstrika', 'Stage 1', 'Zebstrika'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name',
    family_id=522,
    abilities=[
        Attack(
            title='Raid',
            game_text='If this Pokémon evolved from Blitzle during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Mach Bolt',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
