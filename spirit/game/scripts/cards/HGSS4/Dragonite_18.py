from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62a0c1c2-df91-5172-8bf9-5aa208eb2c30',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name',
    display_name='Dragonite',
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=18,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Calming Wind',
            game_text='Remove all Special Conditions from Dragonite.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Stamp',
            game_text='Flip 2 coins. If both of them are tails, this attack does nothing. If both of them are heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
