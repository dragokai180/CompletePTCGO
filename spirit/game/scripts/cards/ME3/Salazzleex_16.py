from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="04d72dfc-c6e8-5f3e-a325-e6dcbdffebdb",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzleex.Name",
    display_name="Salazzle ex",
    searchable_by=["Salazzle ex", "Stage 1", "ex", "Salazzleex"],
    subtypes=["Stage 1", "ex"],
    collector_number=16,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Dire Nails",
            game_text="Your opponent's Active Pokémon is now Burned and Poisoned. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
