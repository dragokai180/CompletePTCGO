from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='685b62a2-5c37-552a-99bc-9ae476b7afc8',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name',
    display_name='Beedrill',
    searchable_by=['Beedrill', 'Stage 2', 'Beedrill'],
    subtypes=['Stage 2'],
    collector_number=15,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Nadir Needle',
            game_text="If you have no cards in your hand, this attack does 120 more damage, and your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.GRASS: 2},
            damage=110,
        ),
    ],
)
