from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb708c3d-9b16-5e11-ab22-da791206dcde',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMuk.Name',
    display_name="Team Aqua's Muk",
    searchable_by=["Team Aqua's Muk", 'Stage 1', 'TeamAquasMuk'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasGrimer.Name',
    family_id=88,
    abilities=[
        Ability(
            title='Sludge Festival',
            game_text='The Retreat Cost of each Pokémon in play (except for Team Aqua Pokémon) is Colorless more.',
            passive=standard_passive('The Retreat Cost of each Pokémon in play (except for Team Aqua Pokémon) is Colorless more.'),
        ),
        Attack(
            title='Pester',
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
